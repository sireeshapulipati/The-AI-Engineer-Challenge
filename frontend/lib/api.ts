/**
 * API client for communicating with the FastAPI backend
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface ChatResponse {
  reply: string;
}

export interface ChatError {
  detail: string;
}

/**
 * Sends a message to the chat API and returns the assistant's reply
 * @param message - The user's message to send
 * @returns Promise resolving to the chat response
 * @throws Error if the API request fails
 */
export async function sendMessage(message: string): Promise<ChatResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      const errorData: ChatError = await response.json().catch(() => ({
        detail: `HTTP error! status: ${response.status}`,
      }));
      throw new Error(errorData.detail || `Failed to send message: ${response.statusText}`);
    }

    const data: ChatResponse = await response.json();
    return data;
  } catch (error) {
    if (error instanceof Error) {
      // Network errors or other issues
      if (error.message.includes('fetch')) {
        throw new Error(
          'Unable to connect to the server. Please make sure the backend is running on http://localhost:8000'
        );
      }
      throw error;
    }
    throw new Error('An unexpected error occurred');
  }
}



