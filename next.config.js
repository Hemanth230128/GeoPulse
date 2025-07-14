/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // Enable static export (replaces deprecated `next export`)
  eslint: {
    ignoreDuringBuilds: true,
  },
  images: {
    unoptimized: true, // ✅ Required for 'next/image' in static builds
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'placehold.co',
        port: '',
        pathname: '/**',
      },
    ],
  },
};

module.exports = nextConfig;
