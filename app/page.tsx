'use client'

import { useUser, SignInButton } from '@clerk/nextjs'
import { useState } from 'react'

export default function Home() {
  const { isSignedIn, user } = useUser()
  const [topic, setTopic] = useState('')
  const [language, setLanguage] = useState('English')
  const [apiKey, setApiKey] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState('')

  const generateLesson = async () => {
    if (!apiKey || !topic) {
      alert('Please enter both OpenRouter API key and a topic.')
      return
    }

    setLoading(true)
    setResult('')

    try {
      const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${apiKey}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          model: "meta-llama/llama-3-8b-instruct",
          messages: [{
            role: "user",
            content: `Create a structured study guide and debugging breakdown for '${topic}' in ${language}. Use clear headings, key concepts, and simple explanations.`
          }]
        })
      })

      const data = await response.json()
      if (data.choices && data.choices.length > 0) {
        setResult(data.choices[0].message.content)
      } else {
        setResult("Failed to generate lesson. Check your API key.")
      }
    } catch (err) {
      setResult("An error occurred while connecting to OpenRouter.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mt-10">
      {!isSignedIn ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="text-5xl font-extrabold leading-tight mb-6">
              STUDY DEEPLY. <span className="text-[#00d2ff]">UNDERSTAND FULLY.</span>
            </h2>
            <p className="text-gray-400 text-lg mb-8 max-w-lg">
              Turn complex chapters and debugging blocks into clear, step-by-step lessons powered by Meta Llama.
            </p>
            <SignInButton mode="modal">
              <button className="bg-gradient-to-r from-[#00d2ff] to-[#0077ff] px-8 py-4 rounded-xl font-bold text-lg shadow-xl shadow-cyan-500/30 hover:shadow-cyan-500/60 transition">
                Start learning now →
              </button>
            </SignInButton>
          </div>
          <div className="bg-[#0a192f]/80 border border-cyan-500/20 p-6 rounded-2xl shadow-2xl backdrop-blur-md">
            <span className="text-xs text-[#00d2ff] uppercase tracking-widest font-semibold">Instant Preview</span>
            <h3 className="text-xl font-bold mt-2 text-white">AI-Powered Concept Clarification</h3>
            <p className="text-gray-400 text-sm mt-2">Break down difficult coding logic or academic topics instantly with real-time AI assistance.</p>
            <div className="bg-cyan-500/10 p-3 rounded-lg text-xs text-[#64ffda] mt-4">
              ✨ Real Google & Apple Auth Enabled via Clerk
            </div>
          </div>
        </div>
      ) : (
        <div className="max-w-3xl mx-auto bg-[#0a192f]/90 border border-cyan-500/20 p-8 rounded-2xl shadow-2xl backdrop-blur-md">
          <h2 className="text-2xl font-bold mb-2">Welcome back, <span className="text-[#00d2ff]">{user?.firstName || 'Student'}</span>!</h2>
          <p className="text-gray-400 text-sm mb-6">Enter a topic or code snippet for instant AI generation and debugging.</p>

          <div className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-gray-300 mb-1 uppercase tracking-wider">Topic / Code to Debug</label>
              <input 
                type="text" 
                value={topic} 
                onChange={(e) => setTopic(e.target.value)}
                placeholder="e.g. React useEffect loop / Photosynthesis / Indian Salt March"
                className="w-full bg-[#01060c] border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-[#00d2ff]"
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-semibold text-gray-300 mb-1 uppercase tracking-wider">Language</label>
                <select 
                  value={language} 
                  onChange={(e) => setLanguage(e.target.value)}
                  className="w-full bg-[#01060c] border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-[#00d2ff]"
                >
                  <option>English</option>
                  <option>Hindi / हिंदी</option>
                  <option>Spanish / Español</option>
                  <option>French / Français</option>
                  <option>German / Deutsch</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-gray-300 mb-1 uppercase tracking-wider">OpenRouter API Key</label>
                <input 
                  type="password" 
                  value={apiKey} 
                  onChange={(e) => setApiKey(e.target.value)}
                  placeholder="sk-or-v1-..."
                  className="w-full bg-[#01060c] border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-[#00d2ff]"
                />
              </div>
            </div>

            <button 
              onClick={generateLesson}
              disabled={loading}
              className="w-full bg-gradient-to-r from-[#00d2ff] to-[#0077ff] py-3 rounded-lg font-bold shadow-lg shadow-cyan-500/20 hover:shadow-cyan-500/40 transition mt-4"
            >
              {loading ? "Generating via Meta Llama..." : "Generate Lesson & Debug ⚡"}
            </button>
          </div>

          {result && (
            <div className="mt-8 bg-[#01060c] border border-white/10 p-6 rounded-xl text-gray-200 whitespace-pre-line leading-relaxed">
              <h4 className="text-[#00d2ff] font-bold mb-3 uppercase text-xs tracking-wider">Generated Output:</h4>
              {result}
            </div>
          )}
        </div>
      )}
    </div>
  )
}