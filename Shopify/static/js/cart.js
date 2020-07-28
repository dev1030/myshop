var updateBtns = document.getElementsByClassName('update-cart')


for(var i = 0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var ProductId = this.dataset.product
        var action = this.dataset.action
        console.log('ProductId',ProductId,'action',action)
        console.log('USER:',user)
        if(user == 'AnonymousUser'){
            console.log('not logged in')
        }else{
            updateUserOrder(ProductId, action)
        }

    })
}

function updateUserOrder(ProductId, action){
    var url = '/updateItem/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'ProductId': ProductId,'action': action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:',data)
        location.reload()
    })
}