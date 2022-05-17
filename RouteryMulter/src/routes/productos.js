/* const express=require('express');
const {Router}=require('express');
const productosRouter=Router(); */

import express from "express";
const productosRouter=express.Router() 

productos[{
    id:1,
    title:"calabaza",
    price:800,
    thumnail:"photo1"
},
{   id:2,
    title:"pelota",
    price:200,
    thumnail:"photo3"
}]



productosRouter.get('/',(req,res)=>{
    res.json(productos)
})

// productosRouter.get('/:id',(req,res)=>{
//     const product_id=req.params.id
//     if (product_id==productos.id){
//         res.send(productos.id, productos.title)
//     }else{
//         res.status(400)
//     }
// })

// productosRouter.post('',(req,res)=>{
//     const product_add=req.body
//     product_add.id=productos.lenght +1
//     productos.push({product_add})

//     res.status(200).json(product_add)
// })
// productosRouter.delete('/:id',(req,res)=>{
//     const delet_id=parseInt(req.params.id)
//     if(delet_id in productos.id){
//         res.send({id:"eliminado"})
//     }
// })



// module.exports=productosRouter
export default productosRouter

