import Link from 'next/link';
import { MountainIcon, User } from 'lucide-react';
import { Button } from '@/components/ui/button';

export function Header() {
  return (
    <header className="sticky top-0 z-40 flex h-16 items-center justify-between border-b bg-background px-4 md:px-6">
      <Link href="/" className="flex items-center gap-2 font-semibold">
        <MountainIcon className="h-6 w-6 text-primary" />
        <span className="text-lg">GeoPulse</span>
      </Link>
      <nav>
        <Button variant="ghost" size="icon">
          <User className="h-5 w-5" />
          <span className="sr-only">User Profile</span>
        </Button>
      </nav>
    </header>
  );
}
