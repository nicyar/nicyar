import ProductsDAOMongoDB from "./productsDAOMongoDB.js";
//import ProductsDAOFirebase from "./productsDAOFirebase.js";
import CartDAOMongoDB from "./cartDAOMongoDB.js";
//import CartDAOFirebase from "./cartDAOFirebase.js";

const ProductsDAOFirebase = () => "xd";
const CartDAOFirebase = () => "xd";

const getStorage = () => {
    const storage = process.env.STORAGE || 'mongodb'
    switch (storage) {
      case 'mongodb':
        return {
          products: new ProductsDAOMongoDB(),
          cart: new CartDAOMongoDB()
        }
        break
      default:
        return {
          products: ProductsDAOFirebase(),
          users: CartDAOFirebase()
        }
        break
    }
  }

  export default getStorage;