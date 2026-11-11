type FreshnessChipProps = {
    source: string
    updatedAt: Date | null
}

export default function FreshnessChip({source, updatedAt}: FreshnessChipProps) {
    const label = updatedAt
        ? `Data: ${source} · updated ${updatedAt.toLocaleTimeString()}`
        : `Data: ${source} · not connected yet`

    return (
        <span
            className="inline-flex items-center gap-2 rounded-full border border-zinc-700 bg-zinc-900 px-3 py-1 text-xs text-zinc-300">
          <span className={`h-2 w-2 rounded-full ${updatedAt ? 'bg-accent' : 'bg-amber-400'}`}/>
                {label}
        </span>
    )
}