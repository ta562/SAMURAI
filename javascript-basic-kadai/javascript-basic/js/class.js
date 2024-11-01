class Product{
    constructor(name,price,category){
        this.name=name;
        this.prise=price;
        this.category=category;
    }
}

const shampoo=new Product('シャンプー',500,'生活雑貨');
const coffee=new Product('コーヒー',1500,'飲料');
console.log(shampoo)
console.log(coffee)