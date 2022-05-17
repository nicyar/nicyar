/* const express=require('express');
const {Router}=express;
const productosRouter=require('./routes/productos')
 */

import express from 'express'
import productosRouter from './routes/app.js' 

const app=express();


app.use(express.json())
app.use(express.urlencoded({extended:true}))

const PORT =8080;
app.listen(PORT,()=>{
    console.log(`listening to port ${PORT}`)
});


app.use('/api/productos',productosRouter)





