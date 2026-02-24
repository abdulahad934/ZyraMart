import React from 'react'
import AdminNavber from './AdminNavber'
import AdminSidebar from './AdminSidebar'


const AdminLayout = ({ children }) => {
  return (
    <div className='d-flex'>
        <AdminSidebar/>
        <div className='w-100'>
            <AdminNavber/>
            <div className='container-fluid mt-3'>
                {children}

            </div>
        </div>

    </div>
  )
}

export default AdminLayout