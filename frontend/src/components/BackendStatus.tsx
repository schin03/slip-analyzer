import { useBackendStatus } from '../hooks/useBackendStatus'

export default function BackendStatus() {
    const state = useBackendStatus()

    const dot =
        state.status === 'online'
            ? 'bg-emerald-400'
            : state.status === 'checking'
                ? 'bg-zinc-500'
                : 'bg-red-400'

    const label =
        state.status === 'online'
            ? 'Backend: online'
            : state.status === 'checking'
                ? 'Backend: checking…'
                : 'Backend: unreachable'

    return (
        <span
            className="inline-flex items-center gap-2 rounded-full border border-zinc-800 px-3 py-1 text-xs text-zinc-300"
            title={state.status === 'offline' ? state.message : undefined}
        >
      <span className={`h-2 w-2 rounded-full ${dot}`} />
            {label}
    </span>
    )
}