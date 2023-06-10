function addComment(csrf_token, productId, endpointUrl) {
  const userName = $('#userName').val()
  const commentText = $('#commentText').val()
  let isValid = true

  $('.warn').map(function () {
    $(this).remove()
  })

  if (!userName) {
    isValid = false

    $('#userName').parent().prepend(`
      <div class='warn'>Это поле обязательное</div>
    `)
  }

  if (!commentText) {
    isValid = false

    $('#commentText').parent().prepend(`
      <div class='warn'>Это поле обязательное</div>
    `)
  }

  if (!isValid) return

  $.ajax({
    url: endpointUrl,
    method: 'POST',
    dataType: 'json',
    data: { csrfmiddlewaretoken: csrf_token, userName: userName, commentText: commentText, productId: productId },
    success: (data) => {
      $('#createCommentForm').after(`
        <div class="comment">
          <div class="comment__avatar">
            <img src="https://med-standart.org/upload/iblock/3d7/m59w4orjj6j02y1gw1xfj6pzthmw2ggx.jpg" alt="avatar">
          </div>

          <div class="comment__content">
            <div class="comment__userName">
              ${userName}
            </div>

            <div class="comment__text">
              ${commentText}
            </div>
          </div>
        </div>
      `)
    }
  })
}