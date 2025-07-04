import Link from 'next/link';
import { MountainIcon } from 'lucide-react';

export function Header() {
  return (
    <header className="sticky top-0 z-40 flex h-16 items-center gap-4 border-b bg-background px-4 md:px-6">
      <Link href="/" className="flex items-center gap-2 font-semibold">
        <MountainIcon className="h-6 w-6 text-primary" />
        <span className="text-lg">Geopulse Navigator</span>
      </Link>
    </header>
  );
}
