'use client';

import Link from 'next/link';

export function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-20 items-center justify-center">
        <Link href="/" className="flex items-center">
          <span className="text-3xl font-bold sm:text-4xl font-headline">
            GeoPulse
          </span>
        </Link>
      </div>
    </header>
  );
}
