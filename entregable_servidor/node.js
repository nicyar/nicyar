// const express=require('express');


// const app=express()

// const PORT=8080

// const server=app.listen(PORT,()=>{
//     console.log(`servidor corriendo en ${PORT}`);
// })

// app.get('/productos',(req,res)=>{
   
//     async function agregar(){
//         try{
//             let products= await JSON.parse(fs.promises.readFile('productos.txt','utf-8')) 
//             res.send({
//                 items:products
//             });
//         }catch(err){
//             res.send(err)
//         }
//     };
//     agregar()
// });

// app.get('/productosRandom',(req,res)=>{
//     async function random(){
//         try{
//             let products= await JSON.parse(fs.promises.readFile('productos.txt','utf-8')) 
//             const randomNum = (min, max) => Math.round(Math.random() * max + min);
//             let randomNumber = randomNum(0, parsed.length - 1);
//             res.send({ Items: products[randomNumber] })
            
//         }catch(err){
//             res.send(err)
//         }
//     };
//     random()


// });

let express = require("express");
const fs = require("fs")

const app = express();

const PORT= process.env.PORT||8080;
const server=app.listen(PORT,()=>{
    console.log(`servidor http escuchando el puerto ${PORT}`);
})



app.get('/products',(req,res)=>{
    let products=JSON.parse(fs.readFileSync('productos.txt','utf-8'))
    

    res.send({
        items:products,
    });
});

app.get('/productsRandom',(req,res)=>{
    let products=fs.readFileSync('productos.txt','utf-8');
    let parsed = JSON.parse(products);
    const randomNum = (min, max) => Math.round(Math.random() * max + min);
    let randomNumber = randomNum(0, parsed.length - 1);
  

    res.send({ Item: parsed[randomNumber] });


})