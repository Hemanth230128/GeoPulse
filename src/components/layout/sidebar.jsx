'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { cn } from '@/lib/utils';
import { Card, CardContent } from '@/components/ui/card';

export function Sidebar({ items, sectionTitle }) {
  const pathname = usePathname();

  return (
    <aside className="w-full md:w-64 flex-shrink-0">
      <Card className="shadow-md">
        <CardContent className="p-4">
          <h2 className="mb-4 text-lg font-semibold capitalize font-headline">{sectionTitle}</h2>
          <nav className="flex flex-col gap-1">
            {items.map((item, index) => (
              <Link
                key={index}
                href={item.href}
                className={cn(
                  'px-3 py-2 rounded-md text-sm font-medium transition-all duration-200 ease-in-out',
                  pathname === item.href
                    ? 'bg-primary text-primary-foreground shadow-sm'
                    : 'hover:bg-accent/50 hover:text-accent-foreground hover:translate-x-1'
                )}
              >
                {item.title}
              </Link>
            ))}
          </nav>
        </CardContent>
      </Card>
    </aside>
  );
}
