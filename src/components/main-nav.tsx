'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { cn } from '@/lib/utils';
import { sections } from '@/lib/sections';

export function MainNav({ mobile = false }) {
  const pathname = usePathname();

  const navClass = cn(
    'flex gap-4',
    mobile
      ? 'flex-col items-start'
      : 'flex-row items-center justify-center text-sm font-medium'
  );

  return (
    <div className={navClass}>
      {sections.map((section) => (
        <Link
          key={section.id}
          href={section.href}
          className={cn(
            'transition-colors hover:text-accent',
            pathname.startsWith(section.href)
              ? 'text-accent'
              : 'text-foreground/80',
            mobile ? 'text-lg' : 'text-sm'
          )}
        >
          {section.title}
        </Link>
      ))}
    </div>
  );
}
