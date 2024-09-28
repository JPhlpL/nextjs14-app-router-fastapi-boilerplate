'use client'
import { useAuth } from '@/hooks/useAuth'

export default function Home() {
  const { user } = useAuth()

  if (!user) {
    return null // The useAuth hook will handle redirection
  }

  return (
    <div className="bg-white shadow rounded-lg p-6">
      <h1 className="text-2xl font-semibold mb-4">Welcome {user.firstname}! </h1>
      <p className="text-gray-600">
        This is a sample page content. You can add your own components and
        content here.
      </p>
    </div>
  );
}
