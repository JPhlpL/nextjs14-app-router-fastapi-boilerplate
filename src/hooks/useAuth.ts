'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'

interface UserData {
  id: string
  email: string
  username: string
  firstname: string
  lastname: string
}

export function useAuth() {
  const [user, setUser] = useState<UserData | null>(null)
  const [loading, setLoading] = useState(true)
  const router = useRouter()

  useEffect(() => {
    async function loadUserFromToken() {
      try {
        const response = await fetch('/api/auth/', {
          credentials: 'include'
        })
        if (response.ok) {
          const userData = await response.json()
          setUser(userData)
        } else {
          setUser(null)
          router.push('/login')
        }
      } catch (error) {
        console.error('Error fetching user data:', error)
        setUser(null)
        router.push('/login')
      } finally {
        setLoading(false)
      }
    }

    loadUserFromToken()
  }, [router])

  return { user, loading }
}