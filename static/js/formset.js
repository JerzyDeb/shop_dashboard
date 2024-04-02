const addRow = (btn) => {
    // Getting formset data from button:
    const formsetData = $(btn).data();
    const formItemClassName = formsetData['formItemClassName']
    const formsetContainerId = formsetData['formsetContainerId']
    const totalFormsPlaceholderId = formsetData['totalFormsPlaceholderId']
    const formPrefix = formsetData['formPrefix']

    // Getting total forms number:
    const $totalForms = $(`#${totalFormsPlaceholderId}`)
    const totalFormsNumber = parseInt($totalForms.attr('value'))

    // Clone hidden row with form and set his number by replace correct regex:
    const $newForm = $(`.${formItemClassName}.d-none`).last().clone()
    const formRegex = RegExp(`${formPrefix}(\\d){1}-`, 'g')
    $newForm.removeClass('d-none')
    $newForm.html($newForm.html().replace(formRegex, `${formPrefix}${totalFormsNumber}-`))

    // Put cloned form at the end of table and implicate form number:
    $(`#${formsetContainerId} tr:last`).prev().after($newForm)
    $totalForms.attr('value', `${totalFormsNumber + 1}`)
}

const removeRow = (btn) => {
    const formsetData = $(btn).data();
    const formItemClassName = formsetData['formItemClassName']
    $(btn).closest(`.${formItemClassName}`).toggle()
    $(btn).closest(`.${formItemClassName}`).find('input[name$="-DELETE"]').val(true)
}