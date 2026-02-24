import {BrowserRouter, Routes, Route} from 'react-router-dom'
import AdminLogin from './components/AdminLogin'
import AdminDashboard from './pages/AdminDashboard'


function App() {
  

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/admin-login" element={<AdminLogin/>} />
        <Route path="/admin-dashboard" element={<AdminDashboard/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
