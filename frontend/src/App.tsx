import Footer from './components/Footer'
import Header from './components/Header'

export default function App() {
    return (
        <div className="flex min-h-screen flex-col">
            <Header />
            <main className="mx-auto w-full max-w-6xl flex-1 px-6 py-10">
                <h2 className="text-xl font-semibold">Top Picks</h2>
                <p className="mt-2 text-zinc-400">Picks will appear here once data is connected.</p>
            </main>
            <Footer />
        </div>
    )
}