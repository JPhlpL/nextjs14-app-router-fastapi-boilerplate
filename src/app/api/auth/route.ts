import { NextResponse } from 'next/server'
import * as jose from 'jose'
import { cookies } from 'next/headers'

const JWT_SECRET = process.env.JWT_SECRET

if (!JWT_SECRET) {
  throw new Error('JWT_SECRET is not set in environment variables')
}

export async function GET() {
  const cookieStore = cookies()
  const token = cookieStore.get('token')?.value

  if (!token) {
    return NextResponse.json({ error: 'Not authenticated' }, { status: 401 })
  }

  try {
    const { payload } = await jose.jwtVerify(token, new TextEncoder().encode(JWT_SECRET))
    return NextResponse.json(payload)
  } catch (error) {
    console.error('JWT verification error:', error)
    return NextResponse.json({ error: 'Invalid token' }, { status: 401 })
  }
}