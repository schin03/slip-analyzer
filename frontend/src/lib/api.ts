const API_URL = import.meta.env.VITE_API_URL as string | undefined

function apiUrl(path: string): string {
    if (!API_URL) {
        throw new Error('VITE_API_URL is not set. Copy .env.example to .env.local.')
    }
    return `${API_URL}${path}`
}

export type HealthResponse = { status: string }

export async function fetchHealth(signal?: AbortSignal): Promise<HealthResponse> {
    const res = await fetch(apiUrl('/health'), { signal })
    if (!res.ok) {
        throw new Error(`Backend responded with HTTP ${res.status}`)
    }
    return (await res.json()) as HealthResponse
}