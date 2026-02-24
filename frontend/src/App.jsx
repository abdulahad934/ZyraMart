import {BrowserRouter, Routes, Route} from 'react-router-dom'
import AdminLogin from './components/AdminLogin'
import AdminDashboard from './pages/AdminDashboard'
import AddProduct from './pages/AddProduct'
import AllProducts from './pages/AllProducts'
import AddCategory from './pages/AddCategory'
import Allcategories from './pages/Allcategories'
import AddBrand from './pages/AddBrand'
import AllBrands from './pages/AllBrands'


function App() {
  

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/admin-login" element={<AdminLogin/>} />
        <Route path="/admin-dashboard" element={<AdminDashboard/>} />
        <Route path="/add-product" element={<AddProduct/>} />
        <Route path="/all-products" element={<AllProducts/>} />
        <Route path="/add-category" element={<AddCategory/>} />
        <Route path="/all-categories" element={<Allcategories/>} />
        <Route path="/add-brand" element={<AddBrand/>} />
        <Route path="/all-brands" element={<AllBrands/>} />
        
      </Routes>
    </BrowserRouter>
  )
}

export default App
