"""Recommendations utils."""

# Standard Library
from collections import Counter

# Django
from django.utils.translation import gettext_lazy as _

# 3rd-Party
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Project
from apps.products.models import Product

# Local
from .models import UserProductInteraction


def get_recommended_products_by_interactions(user_id, similarity_threshold=0.4):
    """
    Generate product recommendations for a given user based on interactions from similar users.

    Args:
        user_id (int): The ID of the user for whom recommendations are to be generated.
        similarity_threshold (float): The minimum similarity score required for a user to be considered similar.

    Returns:
        List[Product]: A sorted list of recommended products, ordered by the number of recommendations.

    Raises:
        ValueError: If the provided user ID is not found in the interaction data.
    """  # noqa: E501

    interactions = UserProductInteraction.objects.values(
        'user_id',
        'product_id',
        'interaction_type',
    )
    df = pd.DataFrame(list(interactions))

    interactions_weight = {
        UserProductInteraction.InteractionType.VIEW: 1,
        UserProductInteraction.InteractionType.ADD_TO_CART: 2,
        UserProductInteraction.InteractionType.RATE: 3,
        UserProductInteraction.InteractionType.PURCHASE: 4,
    }
    df['weight'] = df['interaction_type'].map(interactions_weight)
    interaction_summary = df.groupby([
        'user_id',
        'product_id',
    ]).agg({'weight': 'sum'}).reset_index()

    user_product_matrix = interaction_summary.pivot_table(
        index='user_id',
        columns='product_id',
        values='weight',
        fill_value=0,
    )

    similarity_matrix = cosine_similarity(user_product_matrix)

    if user_id not in user_product_matrix.index:
        raise ValueError(_('Błąd podczas pobierania rekomendacji dla podanego użytkownika'))

    user_idx = user_product_matrix.index.get_loc(user_id)
    user_similarities = similarity_matrix[user_idx]
    similar_users_indices = np.argsort(similarity_matrix[user_idx])[::-1]
    similar_users_indices = [
        idx
        for idx in similar_users_indices
        if user_similarities[idx] > similarity_threshold
    ]
    recommendations = Counter()
    for similar_user_idx in similar_users_indices[1:]:
        similar_user_id = user_product_matrix.index[similar_user_idx]
        similar_user_products = user_product_matrix.loc[similar_user_id][
            user_product_matrix.loc[similar_user_id] > 0].index

        for product_id in similar_user_products:
            recommendations[product_id] += 1

    top_5_recommendations = dict(recommendations.most_common(5))
    products = Product.objects.filter(id__in=top_5_recommendations.keys())
    for product in products:
        product.recommendation_count = top_5_recommendations.get(product.id)
    return sorted(products, key=lambda p: p.recommendation_count, reverse=True)