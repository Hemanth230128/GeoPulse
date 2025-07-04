import Link from 'next/link';
import { MountainIcon } from 'lucide-react';
import { Button } from '@/components/ui/button';

export function Header() {
  return (
    <header className="sticky top-0 z-40 flex h-16 items-center justify-between border-b bg-background px-4 md:px-6">
      <Link href="/" className="flex items-center gap-2 font-semibold">
        <MountainIcon className="h-6 w-6 text-primary" />
        <span className="text-lg">GeoPulse</span>
      </Link>
      <nav>
        <Button variant="outline">Get Started</Button>
      </nav>
    </header>
  );
}
