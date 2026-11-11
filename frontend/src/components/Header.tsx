import FreshnessChip from './FreshnessChip'

export default function Header() {
    return (
        <header className="border-b border-zinc-800">
            <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
                <div>
                    <h1 className="text-lg font-semibold tracking-tight">Slip Analyzer</h1>
                    <p className="text-sm text-zinc-400">NBA props analysis · educational use only</p>
                </div>
                <FreshnessChip source="mock" updatedAt={null} />
            </div>
        </header>
    )
}