function updateProducts(csrf_token, categoryId, endpointUrl, productEndpoint) {
  $.ajax({
    url: endpointUrl,
    method: 'POST',
    dataType: 'json',
    data: { csrfmiddlewaretoken: csrf_token, categoryId: categoryId },
    success: (data) => {
      $('#products').empty()
      console.log('data', data)
      $('.category').map(function () {
        $(this).removeClass("category-active")
      })

      const $currentCategory = $(`*[data-category-id="${categoryId}"]`)
      $currentCategory.addClass('category-active');

      for (let product of data) {
        $('#products').append(`
        <div class="product">
          <div class="product__wrap">
            <div class="product__image">
              <img src="${product.fields.image}" alt="${product.fields.name}">

              <div class="product__category">
                ${$currentCategory.text()}
              </div>
            </div>

            <div class="product__title">
              <a href="${productEndpoint.split('/').slice(0, productEndpoint.split('/').length - 1).join('/') + '/' + product.pk}">${product.fields.name}</a>
            </div>

            <div class="product__totalPrice">
              <div class="product__price">${product.fields.price}</div>
              <div class="product__perOne">₽/шт</div>

              <div class="product__oldPrice">${Math.floor(product.fields.price * 1.3)} ₽</div>
            </div>
          </div>
        </div>
        `)
      }
    }
  })
}