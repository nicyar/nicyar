import express from "express";
import { uploader } from "../utils.js";
const router=express.Router();



let products=[{
    title: "Fernet",
    price: 1500,
    file: "ninguno",
    id: 1},
    {title: "Fernet",
    price: 1500,
    file: "ninguno",
    id: 2
    }, 
];

router.get('/',(req,res)=>{
    res.send({products})
});
router.get('/:id',(req,res)=>{
    let product_id=req.params.id
    if(product_id in products.id){
        res.send(products)
    }

    // const one = ()=>{if(product_id in products.id){
    //     res.send(one)
    // }}
});
router.get('/',(req,res)=>{
    res.send({status:"success",payload:products})
})
router.post('/',uploader.single('file'),(req,res)=>{
    console.log(req.file);
    let product = req.body;
    product.picture = req.file.filename;
    if(product.title && product.price && product.picture){
     
    products.forEach(product =>{
       product.id=products.length+1
    })
    products.push(product);
    }
 
});
router.put('/:id',(req,res)=>{
    const prodMod = req.body;

    const format = prodMod.title && prodMod.price && prodMod.file

    const prodIndex = products.findIndex(elem => elem.id === Number(req.params.id))

    const producto = products.find(elem => elem.id === Number(req.params.id));

    if (format && producto) {
        prodMod.id = products[prodIndex].id;
        products[prodIndex] = prodMod;
        return res.send("Producto modificado");
    } 

    if (!producto) {
        return res.status(404).send({error: "Producto no encontrado"})
    }

    if (!format) {
        res.send({error: "El formato del producto no es correcto (debe tener un title, un price y un thumbnail"})
    }
});
router.delete('/:id',(req,res)=>{
    let product_id=req.params.id
    if(product_id in this.productos.id){
        product_id.splice(prodIndex, 1)
        res.status(200).send({status:"success",nessage:"Product delete"})
    }
});

export default router;
