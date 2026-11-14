import { useEffect, useState } from 'react'
import { fetchHealth } from '../lib/api'

type BackendState =
    | { status: 'checking' }
    | { status: 'online' }
    | { status: 'offline'; message: string }

export function useBackendStatus(): BackendState {
    const [state, setState] = useState<BackendState>({ status: 'checking' })

    useEffect(() => {
        const controller = new AbortController()

        fetchHealth(controller.signal)
            .then(() => setState({ status: 'online' }))
            .catch((err: unknown) => {
                if (err instanceof DOMException && err.name === 'AbortError') return
                const message = err instanceof Error ? err.message : 'Unknown error'
                setState({ status: 'offline', message })
            })

        return () => controller.abort()
    }, [])

    return state
}