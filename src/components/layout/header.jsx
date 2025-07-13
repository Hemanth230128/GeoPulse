'use client';

import Link from 'next/link';
import { Mountain } from 'lucide-react';

export function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center pl-4">
        <Link href="/" className="flex items-center gap-2">
          <Mountain className="h-6 w-6 text-foreground" />
          <span className="font-bold text-xl text-foreground">
            GeoPulse
          </span>
        </Link>
      </div>
    </header>
  );
}
