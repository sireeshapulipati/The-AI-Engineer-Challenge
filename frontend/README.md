# Frontend - AI Mental Coach

A modern, responsive Next.js frontend for the AI Mental Coach application. This frontend provides a beautiful chat interface that connects to the FastAPI backend.

## Features

- 🎨 Modern, colorful UI with purple, orange, and mint gradients
- 💬 Real-time chat interface with message history
- 📱 Fully responsive design for mobile and desktop
- ⚡ Fast and smooth user experience
- 🎯 Clean, professional design that's both trendy and upbeat

## Prerequisites

- Node.js 18+ and npm (or yarn/pnpm)
- The FastAPI backend running on `http://localhost:8000` (see `/api/README.md` for backend setup)

## Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Running Locally

1. Make sure your FastAPI backend is running on `http://localhost:8000`:
```bash
# From the project root
uv run uvicorn api.index:app --reload
```

2. Start the Next.js development server:
```bash
npm run dev
```

3. Open your browser and navigate to `http://localhost:3000`

The frontend will automatically connect to the backend API. If your backend is running on a different URL, you can set the `NEXT_PUBLIC_API_URL` environment variable:

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000 npm run dev
```

## Building for Production

To create a production build:

```bash
npm run build
npm start
```

## Deployment on Vercel

This frontend is configured to work seamlessly with Vercel:

1. Install Vercel CLI (if not already installed):
```bash
npm install -g vercel
```

2. Deploy:
```bash
vercel
```

3. Set environment variables in Vercel dashboard:
   - `NEXT_PUBLIC_API_URL`: The URL of your deployed backend API (e.g., `https://your-backend.vercel.app`)

## Project Structure

```
frontend/
├── app/              # Next.js app directory
│   ├── layout.tsx    # Root layout component
│   ├── page.tsx      # Main chat page
│   ├── page.module.css # Styles for the chat page
│   └── globals.css   # Global styles
├── lib/              # Utility functions
│   └── api.ts        # API client for backend communication
├── package.json      # Dependencies and scripts
├── tsconfig.json     # TypeScript configuration
└── next.config.js    # Next.js configuration
```

## API Integration

The frontend communicates with the backend through the `/api/chat` endpoint:

- **Endpoint**: `POST /api/chat`
- **Request Body**: `{ "message": "user message here" }`
- **Response**: `{ "reply": "assistant response here" }`

The API client is located in `lib/api.ts` and handles all backend communication with proper error handling.

## Troubleshooting

### Backend Connection Issues

If you see connection errors:
1. Verify the backend is running on `http://localhost:8000`
2. Check that CORS is properly configured in the backend
3. Verify the `NEXT_PUBLIC_API_URL` environment variable if using a custom backend URL

### Build Errors

If you encounter build errors:
1. Make sure all dependencies are installed: `npm install`
2. Clear the Next.js cache: `rm -rf .next`
3. Try a fresh install: `rm -rf node_modules && npm install`
