let num=Math.floor(Math.random()*100);

if (num%3===0 && num%5===0){
    console.log(num+'は３と５の倍数です')
}

else if (num%3===0){
    console.log(num+'は３の倍数です')
}

else if (num%5===0){
    console.log(num+'は５の倍数です')
}

else{
    console.log(num)
}
