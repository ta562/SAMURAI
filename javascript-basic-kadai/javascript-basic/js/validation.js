const button=document.getElementById('check-btn');
button.addEventListener('click',validation)
function validation(){
    const name=document.getElementById('name').value;
    const email=document.getElementById('email').value;
    const output= document.getElementById('output');
    let errors=[]
        if(name.trim()===''){
            errors.push('お名前を入力仕手ください')
        }else if(name.length>10){
            errors.push('お名前が10文字を超えています')
        }
        const emailPattern=/^[a-zA-Z0-9.]+@[a-zA-Z0-9.]+$/;
        if(!emailPattern.test(email)){
            errors.push('メールアドレスの入力形式が正しくありません')
        }
        if(errors.length>0){

            output.innerHTML=errors.join('<br>');
        }else{
            output.innerHTML='';
            alert('バリテーションクリア');
        }
}