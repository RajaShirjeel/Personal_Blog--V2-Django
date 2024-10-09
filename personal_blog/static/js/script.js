'use strict'


// Password hide/show
document.addEventListener('DOMContentLoaded', ()=>{
    const passwordIcon = document.getElementById('password-icon');
    const passwordInput = document.getElementById('password-input');

    passwordIcon.addEventListener('click', function(){
        const type = passwordInput.getAttribute('type') === 'password' ? 'text': 'password';
        passwordInput.setAttribute('type', type);
        this.name = type === 'password' ? 'eye-outline': 'eye-off-outline'
    })
})
