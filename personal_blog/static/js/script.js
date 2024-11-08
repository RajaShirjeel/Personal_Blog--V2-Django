'use strict'


// Password hide/show
document.addEventListener('DOMContentLoaded', ()=>{
    try{
        const passwordIcon = document.getElementById('password-icon');
        const passwordInput = document.getElementById('password-input');
    
        passwordIcon.addEventListener('click', function(){
            const type = passwordInput.getAttribute('type') === 'password' ? 'text': 'password';
            passwordInput.setAttribute('type', type);
            this.name = type === 'password' ? 'eye-outline': 'eye-off-outline'
        })
    }

    catch(err){
    }

})

// Comment btn show
try{
    const commentInput = document.querySelector('.comment-input')
    const commentBtn = document.querySelector('.comment-btn')
    
    commentInput.addEventListener('focus', () => {
        commentBtn.style.display = 'block'
    })
}
catch(err){

}
