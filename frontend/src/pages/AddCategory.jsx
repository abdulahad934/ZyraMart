import React, { useState, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { toast, ToastContainer } from 'react-toastify'
import '../styles/addcategory.css'

const generateSlug = (text) =>
  text.toLowerCase().trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '')

const AddCategory = () => {
  const navigate = useNavigate()

  const [form, setForm] = useState({ name: '', slug: '', parent: '', is_active: true })
  const [parents, setParents] = useState([])
  const [errors, setErrors] = useState({})
  const [loading, setLoading] = useState(false)
  const [slugLocked, setSlugLocked] = useState(false)

  // ── Auth Guard ──────────────────────────────────────────────────────────────
  useEffect(() => {
    const token = localStorage.getItem('accessToken')
    if (!token) {
      toast.error('Please login first!')
      navigate('/admin-login')
    }
  }, [navigate])

  useEffect(() => {
    // Parent categories load করতে uncomment করুন:
    // fetch('http://127.0.0.1:8000/api/products/categories/')
    //   .then(res => res.json())
    //   .then(data => setParents(data))
  }, [])

  useEffect(() => {
    if (!slugLocked) {
      setForm(prev => ({ ...prev, slug: generateSlug(prev.name) }))
    }
  }, [form.name, slugLocked])

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target
    setForm(prev => ({ ...prev, [name]: type === 'checkbox' ? checked : value }))
    if (errors[name]) setErrors(prev => ({ ...prev, [name]: '' }))
  }

  const handleSlugChange = (e) => {
    setSlugLocked(true)
    setForm(prev => ({ ...prev, slug: e.target.value }))
    if (errors.slug) setErrors(prev => ({ ...prev, slug: '' }))
  }

  const validate = () => {
    const e = {}
    if (!form.name.trim()) e.name = 'Category name is required'
    if (!form.slug.trim()) e.slug = 'Slug is required'
    return e
  }

 const handleSubmit = async (e) => {
  e.preventDefault()

  const errs = validate()
  if (Object.keys(errs).length) {
    setErrors(errs)
    return
  }

  setLoading(true)

  try {
    const token = localStorage.getItem('accessToken', data.success)

    const response = await fetch(
      'http://127.0.0.1:8000/api/products/add_category/',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify(form)
      }
    )

    const data = await response.json()

    if (!response.ok) {
      if (response.status === 401) {
        toast.error('Session expired. Please login again.')
        
        return
      }

      setErrors(data.errors || {})
      toast.error(data.message || 'Failed to create category!')
      return
    }

    toast.success(data.message || 'Category created successfully!')
    navigate('/all-categories')

  } catch (error) {
    toast.error('Server connection error.')
  } finally {
    setLoading(false)
  }
}

  return (
    <div className="acat-page">
      <ToastContainer position="top-right" autoClose={2000} hideProgressBar={false} newestOnTop={false} closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover theme="colored" />

      <div className="acat-header">
        <div>
          <h1 className="acat-title">Add Category</h1>
          <p className="acat-sub">Create a new product category</p>
        </div>
        <Link to="/all-categories" className="acat-link-btn">All Categories</Link>
      </div>

      <div className="acat-card">
        <form onSubmit={handleSubmit} noValidate>

          {/* Category Name */}
          <div className={`acat-field ${errors.name ? 'acat-field--err' : ''}`}>
            <label className="acat-label">Category Name <span>*</span></label>
            <input
              type="text"
              name="name"
              className="acat-input"
              placeholder="e.g. Men's Footwear"
              value={form.name}
              onChange={handleChange}
              autoFocus
            />
            {errors.name && <p className="acat-err">{errors.name}</p>}
          </div>

          {/* Slug */}
          <div className={`acat-field ${errors.slug ? 'acat-field--err' : ''}`}>
            <label className="acat-label">
              Slug <span>*</span>
              <em>auto-generated</em>
            </label>
            <div className="acat-slug-wrap">
              <span className="acat-slug-prefix">/categories/</span>
              <input
                type="text"
                name="slug"
                className="acat-input acat-input--slug"
                placeholder="mens-footwear"
                value={form.slug}
                onChange={handleSlugChange}
              />
              {slugLocked && (
                <button
                  type="button"
                  className="acat-reset-slug"
                  onClick={() => {
                    setSlugLocked(false)
                    setForm(prev => ({ ...prev, slug: generateSlug(prev.name) }))
                  }}
                >↺</button>
              )}
            </div>
            {errors.slug && <p className="acat-err">{errors.slug}</p>}
          </div>

          {/* Parent Category */}
          <div className="acat-field">
            <label className="acat-label">Parent Category <em>optional</em></label>
            <select name="parent" className="acat-select" value={form.parent} onChange={handleChange}>
              <option value="">— None (Top-level) —</option>
              {parents.map(c => <option key={c.id} value={c.id}>{c.name}</option>)}
            </select>
          </div>

          {/* Status */}
          <div className="acat-field">
            <label className="acat-label">Status</label>
            <label className="acat-toggle">
              <input type="checkbox" name="is_active" checked={form.is_active} onChange={handleChange} />
              <span className="acat-track"><span className="acat-thumb" /></span>
              <span className={`acat-status-text ${form.is_active ? 'active' : 'inactive'}`}>
                {form.is_active ? 'Active' : 'Inactive'}
              </span>
            </label>
          </div>

          {/* Actions */}
          <div className="acat-actions">
            <Link to="/all-categories" className="acat-btn acat-btn--ghost">Cancel</Link>
            <button type="submit" className="acat-btn acat-btn--primary" disabled={loading}>
              {loading && <span className="acat-spinner" />}
              {loading ? 'Saving…' : 'Create Category'}
            </button>
          </div>

        </form>
      </div>
    </div>
  )
}

export default AddCategory