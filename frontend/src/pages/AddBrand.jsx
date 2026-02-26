import React, { useState, useEffect } from 'react'
import { data, Link, useNavigate } from 'react-router-dom'
import { toast, ToastContainer } from 'react-toastify'
import '../styles/addbrand.css'


const AddBrand = () => {
  const navigate = useNavigate();
  const[formData, setFormData] = useState({name: '', slug: '', is_active: true, logo: null})
  const [errors, setErrors] = useState({})
  const [loading, setLoading] = useState(false)

  const validate = () =>{
    const e = {}
    if(!formData.name.trim()) e.name = 'Category name is required'
    if(!formData.slug.trim) e.slug = 'Slug is required'
    return e
  }

  const handleSubmit = async(e) =>{
    e.preventDefault()

    const errs = validate()
    if(Object.keys(errs).length){
      setErrors(errs)
      return
    }
    setLoading(true)

    try{
      const token = localStorage.getItem('accessToken')
      const response = await fetch('http://127.0.0.1:8000/api/products/add-brand',{
        method: 'POST',
        headers:{
          'Cntent-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify(formData)
      })
      const data = await response.json()
      if(!response.ok){
        toast.success(data.message || 'Brand created successfully!')
        navigate('/all-categories')

      }else{
        toast.error(data.message || " Failed to create Brand")
      }
    }catch (error){
      toast.error("Server connection error.")
      console.log(error)
    }finally{
      setLoading(false)
    }
  }

  return (
    <div>AddBrand</div>
  )
}

export default AddBrand