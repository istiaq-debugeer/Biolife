const form=document.getElementById('my_form')
const textcomment=document.getElementById('textcomment')
const csrf=document.getElementsByName('csrfmiddlewaretoken')
const count=document.getElementsById('count')
console.log(form)
console.log(csrf)


form.addEventListener('submit',e=>{
    e.preventDefault()

    const fd=new FormData()
    fd.append('csrfmiddlewaretoken',csrf[0].value)
    fd.append('textcomment',textcomment.value)

    $.ajax({
        type:'POST',
        url:form.getAttribute('action'),
        data: fd,
        success:function(response){
            if (response.success){
                var commentText = $('#textcomment').val();
            }


            $('#textcomment').val('')

            console.log(response)

        },

        error:function (error){
            console.log(error)
        },
        cache:false,
        contentType:false,
        processData:false,
    })
})
console.log(form)