import { ClerkProvider, SignInButton, SignedIn, SignedOut, UserButton } from '@clerk/nextjs'
import './globals.css'

export const metadata = {
  title: 'DRX Academy',
  description: 'AI Study Assistant',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body className="relative bg-[#040d1a] text-white min-h-screen">
          <div className="mandala-flower"></div>
          
          <header className="flex justify-between items-center p-6 border-b border-white/10 relative z-10 max-w-7xl mx-auto">
            <h1 className="text-xl font-bold tracking-wider text-[#00d2ff]">DRX ACADEMY</h1>
            <div>
              <SignedOut>
                <SignInButton mode="modal">
                  <button className="bg-gradient-to-r from-[#00d2ff] to-[#0077ff] px-5 py-2 rounded-lg font-semibold text-sm shadow-lg shadow-cyan-500/20 hover:shadow-cyan-500/40 transition">
                    Sign In / Register
                  </button>
                </SignInButton>
              </SignedOut>
              <SignedIn>
                <UserButton afterSignOutUrl="/" />
              </SignedIn>
            </div>
          </header>

          <main className="relative z-10 max-w-7xl mx-auto p-6">
            {children}
          </main>
        </body>
      </html>
    </ClerkProvider>
  )
}