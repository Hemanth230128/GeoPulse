'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { cn } from '@/lib/utils';

export function Sidebar({ items, sectionTitle }) {
  const pathname = usePathname();

  return (
    <aside className="w-full md:w-64 flex-shrink-0 bg-[#2d3e59] text-gray-200 p-4">
      <h2 className="mb-4 text-lg font-semibold capitalize text-white">{sectionTitle}</h2>
      <nav className="flex flex-col gap-1">
        {items.map((item, index) => (
          <Link
            key={index}
            href={item.href}
            className={cn(
              'block px-3 py-2 rounded-md text-sm font-medium transition-all duration-300 ease-in-out hover:translate-x-1',
              pathname === item.href
                ? 'bg-[#4a5f82] text-white'
                : 'hover:bg-[#3c4d69]'
            )}
          >
            {item.title}
          </Link>
        ))}
      </nav>
    </aside>
  );
}
