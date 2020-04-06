$('#update').click(function(){
    const title = $('#article_title').text()
    const content = $('#article_content').text()
    const pk = $('#article_pk').text()
    $('#article_title').replaceWith("<input text='text' class='form-control d-inline' id='article_title' name='title' value='"+ title+ "'></input>")

    $('#article_content').replaceWith("<textarea text='text' class='form-control' id='article_content' rows='3' name='content'>"+content+ "</textarea>")

    $('#update').replaceWith("<input type='submit' class='btn btn-primary py-1 px-2 ml-2' id='update' value='Save'>")
    $('#delete').replaceWith("<button class='btn btn-secondary py-1 px-2 ml-2' id='cancel'><a class='text-white text-decoration-none' href='/articles/" + pk +"/detail/'>Cancel</a></button>")
})

