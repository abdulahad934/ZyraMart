import React, { useState } from 'react'
import { toast, ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'
import { FaUser, FaLock, FaSignInAlt } from 'react-icons/fa'
import '../styles/adminlogin.css'

const AdminLogin = () => {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleLogin = async (e) => {
    e.preventDefault()

    try {
      const response = await fetch('http://127.0.0.1:8000/api/users/admin-login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      })

      const data = await response.json()

      if (response.ok) {
        toast.success(data.message || 'Login successful!')
        localStorage.setItem('accessToken', data.access)
        localStorage.setItem('refreshToken', data.refresh)
        setTimeout(() => {
            window.location.href = '/admin-dashboard'
        }, 1500)
        } else {
        toast.error(data.error || 'Login failed. Please check your credentials.')
        }

    } catch (error) {
      toast.error('Server error. Try again later.')
      console.error('Login error:', error)
    }
  }

  return (
    <div className="d-flex vh-100 align-items-center justify-content-center position-relative login-bg">
      <div className="card login-card shadow-lg">
        <h4 className="text-center mb-4 text-primary fw-bold">
          <FaLock className="me-2" /> Admin Login
        </h4>

        <form onSubmit={handleLogin}>
          <div className="mb-3">
            <label className="form-label fw-semibold">
              <FaUser className="me-1" /> Username
            </label>
            <input
              type="text"
              className="form-control"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter admin username"
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label fw-semibold">
              <FaLock className="me-1" /> Password
            </label>
            <input
              type="password"
              className="form-control"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password"
              required
            />
          </div>

          <button type="submit" className="btn btn-primary w-100 mt-3 fw-bold">
            <FaSignInAlt className="me-1" /> Login
          </button>
        </form>
      </div>

      <ToastContainer position="top-right" autoClose={2000} />
    </div>
  )
}

export default AdminLogin