const showChart = (url, chartContainerId) => {
    $.get(url, response => {
        const ctx = $(`#${chartContainerId}`);
        const spinner = ctx.closest('div').find('.spinner-border')
        spinner.toggle()
        new Chart(ctx, {
            type: response.type,
            data: response.data,
            options: response.options
        });
    });
}