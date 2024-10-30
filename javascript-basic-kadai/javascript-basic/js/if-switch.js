let num=Math.floor(Math.random()*40);
console.log(num);
if(num===4){
    console.log('大当たりです');
}
else{
    console.log('はずれです')
}

if(num>10&&num<30){
    console.log('１０より大きく３０より小さい');
}

if(num===10||num===30){
    console.log('変数１０または３０')
}