import React, { useState } from 'react';
import { Upload, Loader2, Copy, Bookmark } from 'lucide-react';
import { toast } from 'sonner';
import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const VisionTool = () => {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(selectedFile);
    }
  };

  const handleGenerate = async () => {
    if (!file) {
      toast.error('Please upload an image first');
      return;
    }

    setLoading(true);
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post(`${API}/generate-hashtags-from-image`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      setResult(response.data);
      toast.success('Hashtags generated successfully!');
    } catch (error) {
      console.error('Error:', error);
      toast.error('Failed to generate hashtags. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(result.result);
    toast.success('Copied to clipboard!');
  };

  const handleSave = () => {
    const saved = JSON.parse(localStorage.getItem('hashtagHeroWishlist') || '[]');
    saved.push({
      id: Date.now(),
      type: 'Image Hashtags',
      content: result.result,
      characterCount: result.character_count,
      platformLimit: result.platform_limit,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('hashtagHeroWishlist', JSON.stringify(saved));
    toast.success('Saved to wishlist!');
  };

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
      {/* Input Section */}
      <div className="space-y-6">
        <div>
          <h2 className="text-2xl font-bold mb-2">Image-to-Hashtag</h2>
          <p className="text-[#A1A1AA] text-sm">Upload a photo and get 30 viral hashtags instantly</p>
        </div>

        <div className="bg-[#0A0A0A] border border-white/10 rounded-2xl p-8">
          <label 
            htmlFor="file-upload" 
            data-testid="vision-file-upload-label"
            className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed border-white/20 rounded-xl cursor-pointer hover:border-[#CCFF00]/50 transition-all bg-black/30"
          >
            {preview ? (
              <img src={preview} alt="Preview" className="w-full h-full object-cover rounded-xl" />
            ) : (
              <div className="flex flex-col items-center">
                <Upload className="w-12 h-12 text-[#A1A1AA] mb-4" />
                <p className="text-white font-medium mb-1">Click to upload image</p>
                <p className="text-[#A1A1AA] text-sm">PNG, JPG, WEBP up to 10MB</p>
              </div>
            )}
            <input
              id="file-upload"
              type="file"
              data-testid="vision-file-input"
              className="hidden"
              accept="image/png,image/jpeg,image/webp"
              onChange={handleFileChange}
            />
          </label>

          {file && (
            <div className="mt-4 text-sm text-[#A1A1AA]">
              Selected: {file.name}
            </div>
          )}

          <button
            onClick={handleGenerate}
            disabled={loading || !file}
            data-testid="vision-generate-button"
            className="w-full mt-6 px-8 py-4 bg-[#CCFF00] text-black font-bold rounded-xl hover:bg-[#B3E600] disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center justify-center gap-2"
          >
            {loading ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                Generating...
              </>
            ) : (
              'Generate Hashtags'
            )}
          </button>
        </div>
      </div>

      {/* Result Section */}
      <div className="space-y-6">
        <div>
          <h2 className="text-2xl font-bold mb-2">Generated Hashtags</h2>
          <p className="text-[#A1A1AA] text-sm">Copy and paste to your post</p>
        </div>

        <div className="bg-[#0A0A0A] border border-white/10 rounded-2xl p-8">
          {result ? (
            <>
              <div className="bg-black/50 rounded-xl p-6 mb-4 min-h-[300px]">
                <p className="text-white font-mono text-sm leading-relaxed whitespace-pre-wrap">
                  {result.result}
                </p>
              </div>

              <div className="flex items-center justify-between mb-4 text-sm">
                <span className="text-[#A1A1AA]">
                  {result.hashtag_count} hashtags • {result.character_count} characters
                </span>
                <span className={result.character_count > result.platform_limit ? 'text-red-400' : 'text-[#CCFF00]'}>
                  {result.character_count} / {result.platform_limit}
                </span>
              </div>

              <div className="flex gap-3">
                <button
                  onClick={handleCopy}
                  data-testid="vision-copy-button"
                  className="flex-1 px-6 py-3 bg-white/5 border border-white/10 rounded-xl hover:bg-white/10 transition-all flex items-center justify-center gap-2"
                >
                  <Copy className="w-4 h-4" />
                  Copy
                </button>
                <button
                  onClick={handleSave}
                  data-testid="vision-save-button"
                  className="flex-1 px-6 py-3 bg-[#CCFF00]/10 border border-[#CCFF00]/30 text-[#CCFF00] rounded-xl hover:bg-[#CCFF00]/20 transition-all flex items-center justify-center gap-2"
                >
                  <Bookmark className="w-4 h-4" />
                  Save
                </button>
              </div>
            </>
          ) : (
            <div className="text-center py-20">
              <div className="inline-flex p-6 bg-white/5 rounded-full mb-4">
                <Upload className="w-12 h-12 text-[#A1A1AA]" />
              </div>
              <p className="text-[#A1A1AA]">Upload an image to generate hashtags</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default VisionTool;