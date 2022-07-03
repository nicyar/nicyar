

import mongoose from "mongoose";

//MONGODB CONFIG
export const db = mongoose.connect("mongodb+srv://datanicyar1:<password>@cluster0.prhdi.mongodb.net/test", 
{ useNewUrlParser: true })


const productSchema = new mongoose.Schema({
    name: {type: String, required: true, max: 25},
    price: {type: Number, required: true},
    stock: {type: Number, required: true},
    photo: {type: String, required: true},
    code: {type: String, required: true, max: 10},
    desc: {type: String, required: true, max: 100},
})

export const productsModel = mongoose.model("Products", productSchema);

const cartSchema = new mongoose.Schema({
    products: {type: [{
        name: {type: String, required: true, max: 25},
        price: {type: Number, required: true},
        stock: {type: Number, required: true},
        photo: {type: String, required: true},
        code: {type: String, required: true, max: 10},
        desc: {type: String, required: true, max: 100},
    }]}
}, { timestamps: true })

export const cartModel = mongoose.model("Carts", cartSchema);
