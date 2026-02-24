import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import {
  FaChevronDown,
  FaChevronUp,
  FaCommentAlt,
  FaEdit,
  FaFile,
  FaList,
  FaSearch,
  FaThLarge,
  FaUsers
} from 'react-icons/fa'
import '../style/adminsidebar.css'

const AdminSidebar = () => {
    const [isOpenMenu, setIsOpenMenu] = useState({
        category: false,
        product: false,
        order: false,
        user: false,
    })
  return (
    <div className='sidebar'>
        <div className='profile-card'>
            <img src="" alt="" />
            

        </div>

    </div>
    
  )
}

export default AdminSidebar