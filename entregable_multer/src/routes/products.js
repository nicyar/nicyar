import express, { query } from "express";
import { title } from "process";
import { uploader } from "../utils.js";
const router=express.Router();

let products=[]

router.get('/',(req,res)=>{
    res.send({products})
});
router.get('/:id',(req,res)=>{
    let product_id=req.params.id
    if(product_id in products.id){
        res.send(products)
    }

});
router.get('/',(req,res)=>{
    res.send({status:"success",payload:products})
})
router.post('/',uploader.single('file'),(req,res)=>{
    console.log(req.file);
    let product = req.body;
    product.picture = req.file.filename;
    products.push(product);
    products.forEach(product =>{
       product.id=products.length+1
    })
    res.status(200).send({status:"success",message:"product added"})
})
router.put('/:id',(req,res)=>{
    let product_id=req.params.id
    if(product_id){
    products={
    price:req.body.price,
    title:req.body.title,
    file:req.body.file
    }
    }
})
router.delete('/:id',(req,res)=>{
    let product_id=req.params.id
    if(product_id in products.id){
        res.status(200).send({status:"success",nessage:"Product delete"})
    }
})

export default router;
