const pushBtn=document.getElementById('btn');
const pushText=document.getElementById('text');

pushBtn.addEventListener('click',()=>{
    setTimeout(()=>{pushText.textContent='ボタンをクリックしました';},2000)
});