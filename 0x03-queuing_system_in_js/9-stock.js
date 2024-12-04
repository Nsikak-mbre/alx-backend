import express from 'express';
import redis from 'redis';
import { promisify } from 'util';


// Create the list of products
const listProducts = [
  { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { id: 4, name: "Suitcase 1050", price: 550, stock: 5 }
];

// Create a Redis client and promisify methods
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Helper function to get a product by ID
function getItemById(id) {
  return listProducts.find(item => item.id === id);
}

// Reserve stock for a product
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Get current reserved stock for a product
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
}

// Initialize stock in Redis for all products
listProducts.forEach(product => {
  reserveStockById(product.id, product.stock);
});

// Create an Express server
const app = express();

// Route to list all products
app.get('/list_products', (req, res) => {
  const products = listProducts.map(item => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  }));

  res.json(products);
});

// Route to get product details and current available stock
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: "Product not found" });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId) || product.stock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: "Product not found" });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId) || product.stock;

  if (currentQuantity <= 0) {
    return res.json({ status: "Not enough stock available", itemId });
  }

  await reserveStockById(itemId, currentQuantity - 1);

  res.json({ status: "Reservation confirmed", itemId });
});

// Start the server
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
