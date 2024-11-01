console.log('処理１')
console.log('処理２')
console.log('処理３')

setTimeout(()=>{
    console.log('処理４（非同期処理）');
},2000);

console.log('処理５')

console.log('処理６')
