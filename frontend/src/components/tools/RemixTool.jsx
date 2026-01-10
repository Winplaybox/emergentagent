import React, { useState } from 'react';
import { Loader2, Copy, Bookmark } from 'lucide-react';
import { toast } from 'sonner';
import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const RemixTool = () => {
  const [postContent, setPostContent] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleGenerate = async () => {
    if (!postContent.trim()) {
      toast.error('Please enter your post content');
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post(`${API}/generate-remix`, {
        post_content: postContent
      });

      setResult(response.data);
      toast.success('Content remixed successfully!');
    } catch (error) {
      console.error('Error:', error);
      toast.error('Failed to remix content. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = (text) => {
    navigator.clipboard.writeText(text);
    toast.success('Copied to clipboard!');
  };

  const handleSave = (platform, content) => {
    const saved = JSON.parse(localStorage.getItem('hashtagHeroWishlist') || '[]');
    saved.push({
      id: Date.now(),
      type: `Remix - ${platform}`,
      content,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('hashtagHeroWishlist', JSON.stringify(saved));
    toast.success('Saved to wishlist!');
  };

  return (
    <div className="space-y-8">
      {/* Input Section */}
      <div className="space-y-6">
        <div>
          <h2 className="text-2xl font-bold mb-2">Remix: One Post, Everywhere</h2>
          <p className="text-[#A1A1AA] text-sm">Adapt your content for Instagram, TikTok, and YouTube instantly</p>
        </div>

        <div className="bg-[#0A0A0A] border border-white/10 rounded-2xl p-8">
          <div className="mb-6">
            <label className="block text-sm font-medium mb-2">Your Original Post</label>
            <textarea
              value={postContent}
              onChange={(e) => setPostContent(e.target.value)}
              data-testid="remix-content-input"
              placeholder="Paste your post content here. It can be a caption, description, or any text content you want to adapt for multiple platforms."
              className="w-full px-4 py-3 bg-black/50 border border-white/10 rounded-xl focus:border-[#CCFF00] focus:ring-1 focus:ring-[#CCFF00] outline-none transition-all h-40 resize-none"
            />
          </div>

          <button
            onClick={handleGenerate}
            disabled={loading}
            data-testid="remix-generate-button"
            className="w-full px-8 py-4 bg-[#CCFF00] text-black font-bold rounded-xl hover:bg-[#B3E600] disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center justify-center gap-2"
          >
            {loading ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                Remixing...
              </>
            ) : (
              'Remix for All Platforms'
            )}
          </button>
        </div>
      </div>

      {/* Results Section */}
      {result && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Instagram */}
          <div className="bg-[#0A0A0A] border border-white/10 rounded-2xl p-6 space-y-4">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500 rounded-xl" />
              <div>
                <h3 className="font-bold">Instagram</h3>
                <p className="text-xs text-[#A1A1AA]">Aesthetic & Community</p>
              </div>
            </div>
            <div className="bg-black/50 rounded-xl p-4 min-h-[200px]">
              <p className="text-sm text-white leading-relaxed">{result.instagram}</p>
            </div>
            <div className="flex gap-2">
              <button
                onClick={() => handleCopy(result.instagram)}
                data-testid="remix-instagram-copy"
                className="flex-1 px-4 py-2 bg-white/5 border border-white/10 rounded-lg hover:bg-white/10 transition-all flex items-center justify-center gap-2 text-sm"
              >
                <Copy className="w-4 h-4" />
                Copy
              </button>
              <button
                onClick={() => handleSave('Instagram', result.instagram)}
                data-testid="remix-instagram-save"
                className="flex-1 px-4 py-2 bg-[#CCFF00]/10 border border-[#CCFF00]/30 text-[#CCFF00] rounded-lg hover:bg-[#CCFF00]/20 transition-all flex items-center justify-center gap-2 text-sm"
              >
                <Bookmark className="w-4 h-4" />
                Save
              </button>
            </div>
          </div>

          {/* TikTok */}
          <div className="bg-[#0A0A0A] border border-white/10 rounded-2xl p-6 space-y-4">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-black rounded-xl flex items-center justify-center text-[#00F0FF] font-bold text-xl">
                ♪
              </div>
              <div>
                <h3 className="font-bold">TikTok</h3>
                <p className="text-xs text-[#A1A1AA]">Trendy & Authentic</p>
              </div>
            </div>
            <div className="bg-black/50 rounded-xl p-4 min-h-[200px]">
              <p className="text-sm text-white leading-relaxed">{result.tiktok}</p>
            </div>
            <div className="flex gap-2">
              <button
                onClick={() => handleCopy(result.tiktok)}
                data-testid="remix-tiktok-copy"
                className="flex-1 px-4 py-2 bg-white/5 border border-white/10 rounded-lg hover:bg-white/10 transition-all flex items-center justify-center gap-2 text-sm"
              >
                <Copy className="w-4 h-4" />
                Copy
              </button>
              <button
                onClick={() => handleSave('TikTok', result.tiktok)}
                data-testid="remix-tiktok-save"
                className="flex-1 px-4 py-2 bg-[#CCFF00]/10 border border-[#CCFF00]/30 text-[#CCFF00] rounded-lg hover:bg-[#CCFF00]/20 transition-all flex items-center justify-center gap-2 text-sm"
              >
                <Bookmark className="w-4 h-4" />
                Save
              </button>
            </div>
          </div>

          {/* YouTube */}
          <div className="bg-[#0A0A0A] border border-white/10 rounded-2xl p-6 space-y-4">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-red-600 rounded-xl flex items-center justify-center text-white font-bold text-xl">
                ▶
              </div>
              <div>
                <h3 className="font-bold">YouTube</h3>
                <p className="text-xs text-[#A1A1AA]">Searchable & Engaging</p>
              </div>
            </div>
            <div className="bg-black/50 rounded-xl p-4 min-h-[200px]">
              <p className="text-sm text-white leading-relaxed">{result.youtube}</p>
            </div>
            <div className="flex gap-2">
              <button
                onClick={() => handleCopy(result.youtube)}
                data-testid="remix-youtube-copy"
                className="flex-1 px-4 py-2 bg-white/5 border border-white/10 rounded-lg hover:bg-white/10 transition-all flex items-center justify-center gap-2 text-sm"
              >
                <Copy className="w-4 h-4" />
                Copy
              </button>
              <button
                onClick={() => handleSave('YouTube', result.youtube)}
                data-testid="remix-youtube-save"
                className="flex-1 px-4 py-2 bg-[#CCFF00]/10 border border-[#CCFF00]/30 text-[#CCFF00] rounded-lg hover:bg-[#CCFF00]/20 transition-all flex items-center justify-center gap-2 text-sm"
              >
                <Bookmark className="w-4 h-4" />
                Save
              </button>
            </div>
          </div>
        </div>
      )}

      {!result && (
        <div className="bg-[#0A0A0A] border border-white/10 rounded-2xl p-8">
          <div className="text-center py-20">
            <div className="inline-flex p-6 bg-white/5 rounded-full mb-4">
              <svg className="w-12 h-12 text-[#A1A1AA]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
              </svg>
            </div>
            <p className="text-[#A1A1AA]">Enter your post to remix it for all platforms</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default RemixTool;